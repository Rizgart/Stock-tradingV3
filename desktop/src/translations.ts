import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  en: {
    translation: {
      navigation: 'Primary navigation',
      dashboard: 'Dashboard',
      recommendations: 'Recommendations',
      watchlist: 'Watchlist & Portfolio',
      settings: 'Settings',
      dashboard_welcome: 'Monitor performance, alerts, and news at a glance.',
      loading: 'Loading…',
      stock_description: 'Latest analytics for {{symbol}}',
      api_key: 'API key',
      api_key_help: 'Store your Massive API key securely. It is kept locally only.',
      language: 'Language',
      desktop_notifications: 'Enable desktop notifications',
      toggle_theme: 'Toggle high contrast mode'
    }
  },
  sv: {
    translation: {
      navigation: 'Primär navigering',
      dashboard: 'Instrumentpanel',
      recommendations: 'Rekommendationer',
      watchlist: 'Bevakningslista & Portfölj',
      settings: 'Inställningar',
      dashboard_welcome: 'Övervaka prestation, aviseringar och nyheter.',
      loading: 'Laddar…',
      stock_description: 'Senaste analysen för {{symbol}}',
      api_key: 'API-nyckel',
      api_key_help: 'Spara din Massive API-nyckel lokalt och säkert.',
      language: 'Språk',
      desktop_notifications: 'Aktivera skrivbordsaviseringar',
      toggle_theme: 'Växla högkontrastläge'
    }
  }
};

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: 'en',
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false
    }
  });

export default i18n;
