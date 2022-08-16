const Path = require('path');

module.exports = {
  context: Path.resolve(__dirname, "src"),
  entry: ["./index1.js",],
  output: {
    path: Path.resolve(__dirname, "../static/frontend/"),
    filename: 'index1.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  },
  mode: 'development'
};