import React from 'react';
import { Link, Outlet } from 'react-router-dom';
import { useTranslation } from 'react-i18next';

import Disclaimer from '../components/Disclaimer';

const App: React.FC = () => {
  const { t } = useTranslation();
  return (
    <div className="app" role="main">
      <nav aria-label={t('navigation')}>
        <ul>
          <li><Link to="/">{t('dashboard')}</Link></li>
          <li><Link to="/recommendations">{t('recommendations')}</Link></li>
          <li><Link to="/watchlist">{t('watchlist')}</Link></li>
          <li><Link to="/settings">{t('settings')}</Link></li>
        </ul>
      </nav>
      <section className="content">
        <Outlet />
      </section>
      <Disclaimer />
    </div>
  );
};

export default App;
