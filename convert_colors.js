const hexToHSL = (hex) => {
    // Remove the hash if present
    hex = hex.replace('#', '');

    // Convert hex to RGB
    const r = parseInt(hex.substring(0, 2), 16) / 255;
    const g = parseInt(hex.substring(2, 4), 16) / 255;
    const b = parseInt(hex.substring(4, 6), 16) / 255;

    const max = Math.max(r, g, b);
    const min = Math.min(r, g, b);
    let h, s, l = (max + min) / 2;

    if (max === min) {
        h = s = 0;
    } else {
        const d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch (max) {
            case r:
                h = (g - b) / d + (g < b ? 6 : 0);
                break;
            case g:
                h = (b - r) / d + 2;
                break;
            case b:
                h = (r - g) / d + 4;
                break;
        }
        h /= 6;
    }

    // Convert to degrees and percentages
    h = Math.round(h * 360);
    s = Math.round(s * 100);
    l = Math.round(l * 100);

    return `hsl(${h}, ${s}%, ${l}%)`;
};

const colors = {
    "ikas": {
        "0": "#f5f8ff",
        "1": "#e8efff",
        "2": "#d1deff",
        "3": "#a9c1ff",
        "4": "#7a9fff",
        "5": "#4c7dff",
        "6": "#3461db",
        "7": "#234ab7",
        "8": "#163393",
        "9": "#0c1d70"
    },
    "slate": {
        "0": "#f8fafc",
        "1": "#eef2f6",
        "2": "#e3e8ef",
        "3": "#cdd5df",
        "4": "#9aa4b2",
        "5": "#697586",
        "6": "#4b5565",
        "7": "#364152",
        "8": "#242b36",
        "9": "#121926"
    },
    "neutral": {
        "0": "#fafafa",
        "1": "#f6f6f6",
        "2": "#ececed",
        "3": "#c4c4c6",
        "4": "#9c9c9f",
        "5": "#727276",
        "6": "#4a4a4f",
        "7": "#2e2e33",
        "8": "#202025",
        "9": "#14141a"
    },
    "indigo": {
        "0": "#f7f5ff",
        "1": "#efedff",
        "2": "#d5cdff",
        "3": "#b2a4ff",
        "4": "#8e7aff",
        "5": "#6f55ff",
        "6": "#5a44d5",
        "7": "#4533ab",
        "8": "#312280",
        "9": "#261a6b"
    },
    "lime": {
        "0": "#fcfef1",
        "1": "#f8fee3",
        "2": "#f2fdc8",
        "3": "#ebfbac",
        "4": "#e5fa91",
        "5": "#dcfb6e",
        "6": "#cce85f",
        "7": "#bad749",
        "8": "#a9c733",
        "9": "#97b61d"
    },
    "blue": {
        "0": "#f2f9fe",
        "1": "#e7f8ff",
        "2": "#c1e3fb",
        "3": "#8fccf8",
        "4": "#4cadf4",
        "5": "#2a9ef2",
        "6": "#2388d1",
        "7": "#1b71af",
        "8": "#145b8e",
        "9": "#10507d"
    },
    "fuchsia": {
        "0": "#fdf2fa",
        "1": "#f9deef",
        "2": "#f4c4e3",
        "3": "#eb97ce",
        "4": "#e679bf",
        "5": "#e05bb1",
        "6": "#c04b97",
        "7": "#c04b97",
        "8": "#a03b7c",
        "9": "#7f2c62"
    },
    "red": {
        "0": "#fff5f6",
        "1": "#ffd8da",
        "2": "#fecdca",
        "3": "#ff8a91",
        "4": "#ff636d",
        "5": "#ff3c48",
        "6": "#db303b",
        "7": "#b7242d",
        "8": "#931820",
        "9": "#76131a"
    },
    "amber": {
        "0": "#fef8f0",
        "1": "#fde9ce",
        "2": "#fddeb5",
        "3": "#fcd39d",
        "4": "#fabc6b",
        "5": "#f9a63a",
        "6": "#f79009",
        "7": "#c67307",
        "8": "#945605",
        "9": "#633a04"
    },
    "green": {
        "0": "#f0fdf5",
        "1": "#d1fadf",
        "2": "#a6f4c5",
        "3": "#6ce9a6",
        "4": "#32d583",
        "5": "#12b76a",
        "6": "#039855",
        "7": "#027a48",
        "8": "#05603a",
        "9": "#054f31"
    }
};

const result = {};

for (const [colorName, shades] of Object.entries(colors)) {
    result[colorName] = [];
    for (const [shade, hex] of Object.entries(shades)) {
        const shadeNum = parseInt(shade);
        const scale = shadeNum === 0 ? 50 : shadeNum * 100;
        result[colorName].push({
            scale: scale,
            hsl: hexToHSL(hex)
        });
    }
}

console.log(JSON.stringify(result, null, 2)); 