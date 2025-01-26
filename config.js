// config.js

// Google Analytics (gtag)
window.dataLayer = window.dataLayer || [];
function gtag() {
  dataLayer.push(arguments);
}
gtag("js", new Date());
gtag("config", "G-XXXXXXXXXX"); // Replace with your Google Analytics ID

// Google Search Console verification
(function () {
  const meta = document.createElement("meta");
  meta.name = "google-site-verification";
  meta.content = "YOUR_VERIFICATION_CODE"; // Replace with your verification code
  document.head.appendChild(meta);
})();

// Additional tags
(function () {
  const customMeta = [
    {
      name: "bing-site-verification",
      content: "YOUR_BING_VERIFICATION_CODE", // Replace with Bing verification code
    },
    {
      name: "yandex-verification",
      content: "YOUR_YANDEX_VERIFICATION_CODE", // Replace with Yandex verification code
    },
  ];
  customMeta.forEach(({ name, content }) => {
    const meta = document.createElement("meta");
    meta.name = name;
    meta.content = content;
    document.head.appendChild(meta);
  });
})();
