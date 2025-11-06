import React from 'react';
import { useTranslation } from 'react-i18next';

const Dashboard: React.FC = () => {
  const { t } = useTranslation();
  return (
    <div>
      <h1>{t('dashboard')}</h1>
      <p>{t('dashboard_welcome')}</p>
    </div>
  );
};

export default Dashboard;
