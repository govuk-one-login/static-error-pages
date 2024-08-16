const path = require("path");
const HtmlBundlerPlugin = require("html-bundler-webpack-plugin");

module.exports = {
  mode: "production",
  devServer: {
    static: {
      directory: path.join(__dirname, "public"),
    },
    compress: true,
    port: 9000,
  },
  output: {
    path: path.join(__dirname, "dist/"),
  },
  plugins: [
    new HtmlBundlerPlugin({
      entry: {
        index: "./src/index.html",
      },
      css: {
        inline: true, // inline CSS into HTML
      },
      js: {
        inline: true, // inline JS into HTML
      },
    }),
  ],
  module: {
    rules: [
      {
        test: /\.(css|sass|scss)$/,
        use: ["css-loader", "sass-loader"],
      },
      // inline all assets: images, svg, fonts
      {
        test: /\.(ico|png|jpe?g|webp|svg|woff2?)$/i,
        type: "asset/inline",
      },
    ],
  },
  performance: false, // disable warning max size
};
