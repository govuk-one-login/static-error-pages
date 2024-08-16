require("expect-puppeteer");
const { AxePuppeteer } = require("@axe-core/puppeteer");
const { createHtmlReport } = require("axe-html-reporter");

describe("Google", () => {
  beforeAll(async () => {
    await page.goto("http://localhost:9000");
  });

  it("should pass accessibility tests", async () => {
    const results = await new AxePuppeteer(page).analyze();
    createHtmlReport({
      results: results,
    });
    expect(results.violations.length).toBe(0);
  });
});
