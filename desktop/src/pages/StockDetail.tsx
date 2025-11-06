import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { useTranslation } from 'react-i18next';

interface StockDetailResponse {
  symbol: string;
  description: string;
  indicators: string[];
}

const StockDetail: React.FC = () => {
  const { symbol } = useParams();
  const { t } = useTranslation();
  const [detail, setDetail] = useState<StockDetailResponse | null>(null);

  useEffect(() => {
    if (!symbol) return;
    axios.get(`/api/recommendations?symbol=${symbol}`).then((response) => {
      const [first] = response.data;
      setDetail({
        symbol: first?.symbol ?? symbol,
        description: t('stock_description', { symbol: first?.symbol ?? symbol }),
        indicators: first?.rationale ?? []
      });
    });
  }, [symbol, t]);

  if (!detail) {
    return <p>{t('loading')}</p>;
  }

  return (
    <article>
      <h1>{detail.symbol}</h1>
      <p>{detail.description}</p>
      <ul>
        {detail.indicators.map((indicator) => <li key={indicator}>{indicator}</li>)}
      </ul>
    </article>
  );
};

export default StockDetail;
