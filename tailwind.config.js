/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      backgroundColor: {
        light: {
          primary: "#F7F8F8",
        },
        dark: {
          primary: "#050F27",
          secondary: "#111B31",
        },
      },
      textColor: {
        light: {
          primary: "#050F27",
        },
      },
      borderColor: {
        light: {
          primary: "#F7F8F8",
        },
        dark: {
          primary: "#050F27",
        },
      },
    },
    fontFamily: {
      inter: ["Inter", "sans-serif"],
    },
  },
  plugins: [],
};
