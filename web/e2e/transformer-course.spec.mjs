import { expect, test } from '@playwright/test'

test('learner can use diagnostic and attention lab', async ({ page }) => {
  await page.goto('/')

  await expect(page.getByRole('heading', { name: /Transformer Mastery Course/i })).toBeVisible()
  await expect(page.getByRole('tab', { name: /Graph/i })).toBeVisible()
  await expect(page.getByText(/A = softmax/i)).toBeVisible()
  await expect(page.locator('.graphNode')).toHaveCount(11)

  await page.getByRole('tab', { name: /Diagnostic/i }).click()
  await page.getByLabel(/Weighted average: 2.6/i).click()
  await page.getByLabel(/Dot product: 11/i).click()
  await page.getByLabel(/Softmax assigns/i).click()
  await page.getByLabel(/tokens\[1\] returns "learn"/i).click()
  await page.getByLabel(/Future tokens get zero attention share/i).click()
  await page.getByRole('button', { name: /Score Diagnostic/i }).click()

  await expect(page.getByText(/Ready for attention core/i)).toBeVisible()

  await page.getByRole('tab', { name: /Attention Lab/i }).click()
  await page.getByLabel(/Mask future tokens/i).check()

  await expect(page.getByText(/Query token/i)).toBeVisible()
  await expect(page.getByText(/Attention Shares/i)).toBeVisible()
  await expect(page.getByRole('cell', { name: 'masked' }).first()).toBeVisible()
})
