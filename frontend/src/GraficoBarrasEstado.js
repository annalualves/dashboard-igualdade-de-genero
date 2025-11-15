import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const API_URL = 'http://localhost:5000/api';

// Perceba o { ano } aqui. É assim que ele recebe o dado do App.js
function GraficoBarrasEstado({ ano }) {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Lógica para decidir qual URL chamar
    // Se 'ano' tiver valor (ex: 2022), adiciona "?ano=2022" na URL. 
    // Se não, chama a rota normal (todos os anos).
    const url = ano ? `${API_URL}/casos_por_estado?ano=${ano}` : `${API_URL}/casos_por_estado`;

    axios.get(url)
      .then(response => {
        // Ordena os dados (maior para menor)
        const sortedData = response.data.sort((a, b) => b.casos - a.casos);
        setData(sortedData);
      })
      .catch(error => console.error('Erro ao buscar dados de casos por estado:', error));
      
  }, [ano]); // O [ano] aqui faz o gráfico recarregar quando você muda o filtro

  return (
    <div className="chart-container full-width-chart">
      {/* Mostra no título se está filtrado ou não */}
      <h3>Casos por Estado (RF01) {ano ? ` - ${ano}` : ''}</h3>
      
      <ResponsiveContainer width="100%" height={400}>
        <BarChart
          data={data}
          margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="id" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="casos" fill="#8B0000" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default GraficoBarrasEstado;