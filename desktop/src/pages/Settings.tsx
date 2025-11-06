import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';

const Settings: React.FC = () => {
  const { t, i18n } = useTranslation();
  const [apiKey, setApiKey] = useState('');
  const [locale, setLocale] = useState(i18n.language);
  const [notificationsEnabled, setNotificationsEnabled] = useState(true);

  const handleLocaleChange = (value: string) => {
    setLocale(value);
    i18n.changeLanguage(value);
  };

  return (
    <form className="settings" aria-label={t('settings')}>
      <h1>{t('settings')}</h1>
      <label>
        {t('api_key')}
        <input
          type="text"
          value={apiKey}
          onChange={(event) => setApiKey(event.target.value)}
          aria-describedby="api-key-help"
        />
      </label>
      <p id="api-key-help">{t('api_key_help')}</p>

      <label>
        {t('language')}
        <select value={locale} onChange={(event) => handleLocaleChange(event.target.value)}>
          <option value="en">English</option>
          <option value="sv">Svenska</option>
        </select>
      </label>

      <label>
        <input
          type="checkbox"
          checked={notificationsEnabled}
          onChange={(event) => setNotificationsEnabled(event.target.checked)}
        />
        {t('desktop_notifications')}
      </label>

      <button type="button" onClick={() => window.electronAPI?.toggleTheme()}>
        {t('toggle_theme')}
      </button>
    </form>
  );
};

export default Settings;
