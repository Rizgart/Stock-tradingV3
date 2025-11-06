import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import App from './pages/App';
import Dashboard from './pages/Dashboard';
import Recommendations from './pages/Recommendations';
import StockDetail from './pages/StockDetail';
import Watchlist from './pages/Watchlist';
import Settings from './pages/Settings';
import './styles.css';
import './translations';

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    children: [
      { index: true, element: <Dashboard /> },
      { path: 'recommendations', element: <Recommendations /> },
      { path: 'stocks/:symbol', element: <StockDetail /> },
      { path: 'watchlist', element: <Watchlist /> },
      { path: 'settings', element: <Settings /> }
    ]
  }
]);

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
