import { expect, test } from '@playwright/test'

test('learner can use lesson-centered course, map, diagnostic, practice, and attention lab', async ({ page }) => {
  await page.goto('/')

  await expect(page.getByRole('heading', { name: /Transformer Mastery Course/i })).toBeVisible()
  await expect(page.getByLabel(/Transformer course knowledge graph/i)).toHaveCount(0)
  await expect(page.getByText(/Ask Before Naming/i)).toBeVisible()

  await page.getByRole('button', { name: /Open Map/i }).click()
  await expect(page.getByLabel(/Transformer course knowledge graph/i)).toBeVisible()
  await expect(page.locator('.graphNode')).toHaveCount(42)
  await page.getByRole('button', { name: /Close Map/i }).click()
  await expect(page.getByLabel(/Transformer course knowledge graph/i)).toHaveCount(0)

  await page.getByRole('button', { name: /^Diagnostic$/i }).click()
  await page.getByRole('button', { name: /Fill Experienced Path/i }).click()
  await page.getByRole('button', { name: /Score Diagnostic/i }).click()

  await expect(page.getByText(/Ready for attention core/i)).toBeVisible()

  await page.getByRole('button', { name: /^Practice$/i }).click()
  await page.getByRole('button', { name: /Identify shared versus position-specific quantities/i }).click()
  await page.getByRole('button', { name: /Mark Mastered/i }).click()
  await expect(page.getByRole('button', { name: /Mastered/i })).toBeVisible()

  await page.getByRole('button', { name: /^Lab$/i }).click()
  await page.getByLabel(/Mask future tokens/i).check()
  await page.getByRole('button', { name: /Reveal Row/i }).click()

  await expect(page.getByText(/Query token/i)).toBeVisible()
  await expect(page.getByText(/Mixed output/i)).toBeVisible()
  await expect(page.getByRole('cell', { name: 'masked' }).first()).toBeVisible()
})
