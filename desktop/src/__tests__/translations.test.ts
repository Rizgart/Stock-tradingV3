import { describe, expect, it } from 'vitest';
import i18n from '../translations';

describe('translations', () => {
  it('provides english strings', () => {
    expect(i18n.t('dashboard')).toBe('Dashboard');
  });
});
