/** @type {import('tailwindcss').Config} */
module.exports = {
content: ["./theme/**/*.html", "./theme/**/*.js"],
theme: {
    extend: {},
},
plugins: [
  require('@tailwindcss/typography'),
],
};
