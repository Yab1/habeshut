const path = require("path");

module.exports = {
  entry: "./src/assets/scripts/entry.js",
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "src", "static", "scripts"),
  },
};
