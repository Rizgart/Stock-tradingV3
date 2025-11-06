import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useTranslation } from 'react-i18next';

interface WatchlistItem {
  symbol: string;
  added_at: string;
}

const Watchlist: React.FC = () => {
  const { t } = useTranslation();
  const [items, setItems] = useState<WatchlistItem[]>([]);
  const userId = 'local-user';

  useEffect(() => {
    axios.get(`/api/watchlists/${userId}`).then((response) => setItems(response.data));
  }, [userId]);

  return (
    <section>
      <h1>{t('watchlist')}</h1>
      <ul>
        {items.map((item) => (
          <li key={item.symbol}>{item.symbol} - {new Date(item.added_at).toLocaleString()}</li>
        ))}
      </ul>
    </section>
  );
};

export default Watchlist;
