// Outside claude.ai there is no window.claude. This static build runs in local mode only:
// 'sample' is unavailable (the Claude toggle stays hidden) and 'downloads' saves files in the browser.
(function () {
  if (window.claude) return;
  const downloads = {
    save: async ({ filename, data }) => {
      const blob = data instanceof Blob ? data : new Blob([data]);
      const url = URL.createObjectURL(blob), a = Object.assign(document.createElement('a'), { href: url, download: filename });
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(url), 10000);
    },
  };

  window.claude = {
    use: async (name) => {
      if (name === 'downloads') return downloads;
      return null;
    },
  };
})();
