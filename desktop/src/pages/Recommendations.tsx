import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useTranslation } from 'react-i18next';

interface Recommendation {
  symbol: string;
  score: number;
  rationale: string[];
}

const Recommendations: React.FC = () => {
  const { t } = useTranslation();
  const [data, setData] = useState<Recommendation[]>([]);

  useEffect(() => {
    axios.get('/api/recommendations').then((response) => setData(response.data));
  }, []);

  return (
    <section>
      <h1>{t('recommendations')}</h1>
      <ul>
        {data.map((item) => (
          <li key={item.symbol}>
            <h2>{item.symbol} - {item.score}</h2>
            <ul>
              {item.rationale.map((factor) => <li key={factor}>{factor}</li>)}
            </ul>
          </li>
        ))}
      </ul>
    </section>
  );
};

export default Recommendations;
