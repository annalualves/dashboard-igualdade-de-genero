import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const API_URL = 'http://localhost:5000/api';

function GraficoTendencia() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get(`${API_URL}/tendencia_anual`)
      .then(response => setData(response.data))
      .catch(error => console.error('Erro ao buscar dados de tendência:', error));
  }, []);

  return (
    <div className="chart-container">
      <h3>Evolução dos Casos (RF03)</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="ano" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="casos" stroke="#8B0000" activeDot={{ r: 8 }} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default GraficoTendencia;