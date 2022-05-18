/* eslint-env node, browser */

"use strict";

const ipc = require("electron").ipcRenderer;
const auxData = require("./index.data.json");

ipc.on("start", function (event, snapshotTasksRaw) {
	let snapshotTasks = [];
	for (const task of snapshotTasksRaw) {
		for (const theme of ["dark", "light"]) {
			for (const bg of ["black", "white"]) {
				snapshotTasks.push({
					...task,
					theme,
					background: bg,
					name: task.name + "." + theme + "." + bg
				});
			}
		}
	}
	let current = 0;
	const step = function () {
		const doit = function () {
			captureElement(snapshotTasks[current], function () {
				current += 1;
				if (current >= snapshotTasks.length) window.close();
				else setTimeout(step, 500);
			});
		};
		setTimeout(doit, 500);
	};
	setTimeout(step, 2000);
});

let onScroll = function () {};
ipc.on("scroll", function () {
	onScroll.apply(this, arguments);
	setTimeout(function () {
		ipc.send("snapshot", "scroll-done");
	}, 500);
});

let onComplete = function () {};
ipc.on("complete", function () {
	onComplete.apply(this, arguments);
});

const captureCallbacks = {
	cbAmendLigsetSamplerContents,
	cbAmendStylisticSetContents,
	cbAmendCharacterVariantContents
};

const ssStrings = [
	["ABC.DEF.GHI.JKL.MNO.PQRS.TUV.WXYZ", "abc.def.ghi.jkl.mno.pqrs.tuv.wxyz"],
	["¢ ſß ΓΛΔ αδιλμξ КУЗЯ эльф язычник", "float il1[]={1-2/3.4,5+6=7/8%90};"],
	["1234567890 ,._-+= >< ¯-¬_ >~–÷+×<", "{}[]()<>`+-=$*/#_%^@\\&|~?'\" !,.;:"],
	["!iIlL17|¦ coO08BbDQ $5SZ2zsz 96G&", [..."dbqp E3 g9q CGQ vvw VVW /V ", "<=", " ", ">="]]
];
function cbAmendStylisticSetContents(element, p) {
	element.innerHTML = "";
	const inner = document.createElement("div");
	inner.className = "inner";
	element.appendChild(inner);

	for (const row of ssStrings) {
		const line = document.createElement("p");
		line.className = "line";
		inner.appendChild(line);
		const sHC = new Set(p.hotChars || []);

		for (const colStr of row) {
			const col = document.createElement("span");
			col.className = "col";
			line.appendChild(col);
			for (const lch of colStr) {
				if (sHC.has(lch)) {
					const b = document.createElement("b");
					b.appendChild(document.createTextNode(lch));
					col.appendChild(b);
				} else {
					col.append(document.createTextNode(lch));
				}
			}
		}
	}
}

function cbAmendLigsetSamplerContents(element, p) {
	element.innerHTML = "";
	if (p.tag === "calt") element.style.fontFeatureSettings = `'${p.tag}' ${p.rank}`;
	else element.style.fontFeatureSettings = `'calt' off, '${p.tag}' ${p.rank}`;

	const groupSet = new Set(p.ligSets);
	for (const row of auxData.ligationSamples) {
		const line = document.createElement("div");
		element.appendChild(line);
		for (let m = 0; m < row.length; m++) {
			if (m > 0) line.appendChild(document.createTextNode(" "));
			const sampleStr = row[m];
			let rank = 0;
			for (const [lgName, lg] of Object.entries(auxData.ligationCherry)) {
				if (!groupSet.has(lg.ligGroup)) continue;
				if (!new Set(lg.samples || []).has(sampleStr)) continue;
				const rankT = lg.sampleRank || 1;
				if (rankT > rank) rank = rankT;
			}
			if (rank) {
				const run = document.createElement("em");
				run.appendChild(document.createTextNode(sampleStr));
				run.className = `rank-${rank}`;
				line.appendChild(run);
			} else {
				const run = document.createElement("s");
				run.appendChild(document.createTextNode(sampleStr));
				run.className = `rank-${rank}`;
				line.appendChild(run);
			}
		}
	}
}

function cbAmendCharacterVariantContents(element, p) {
	element.innerHTML = "";
	const slopeClasses = p.slopeDependent ? ["run", "run italic"] : ["run"];
	element.style.width = p.hotChars.length * slopeClasses.length + "em";
	for (const s of p.hotChars) {
		for (const slopeCls of slopeClasses) {
			const run = document.createElement("span");
			run.className = slopeCls;
			run.appendChild(document.createTextNode(s));
			element.appendChild(run);
		}
	}
}

function captureElement(options, callback) {
	window.scroll(0, 0);
	setTimeout(function () {
		// Set theme
		document.querySelector("body").className =
			`color-${options.theme}` + ` bg-${options.background}`;

		const element = document.querySelector(options.el);
		if (options.applyClass) {
			element.className = options.applyClass;
		}
		if (options.applyFeature) {
			element.style = "font-feature-settings:" + options.applyFeature;
		}
		if (options.applyCallback) {
			captureCallbacks[options.applyCallback](element, options.applyCallbackArgs);
		}
		const rect = element.getBoundingClientRect();
		onScroll = function (event, arg) {
			window.scrollTo(0, arg);
		};
		onComplete = function () {
			if (callback) callback();
			onComplete = function () {};
		};
		ipc.send("snapshot", {
			name: options.name,
			windowWidth: window.innerWidth,
			windowHeight: window.innerHeight,
			doubleTrim: options.doubleTrim,
			dpi: window.devicePixelRatio,
			x: rect.left | 0,
			y: rect.top | 0,
			width: rect.width | 0,
			height: rect.height | 0
		});
	}, 10);
}

window.onload = function () {
	ipc.send("snapshot", "Browser process ready");
};
