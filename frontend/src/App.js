import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { PieChart, Pie, Cell, Tooltip, Legend } from 'recharts';
import './App.css';
import GraficoTendencia from './GraficoTendencia';
import GraficoBarrasEstado from './GraficoBarrasEstado';

const API_URL = 'http://localhost:5000/api';

// --- Componentes Internos Atualizados para receber Filtro ---

function KpiCard({ title, value }) {
  return (
    <div className="kpi-card">
      <h2>{value}</h2>
      <h3>{title}</h3>
    </div>
  );
}

function GraficoTipologia({ ano }) {
  const [data, setData] = useState([]);
  const COLORS = ['#FF8042', '#0088FE', '#FFBB28', '#00C49F'];

  useEffect(() => {
    // Passa o ano na URL: /api/tipologia?ano=2023
    const url = ano ? `${API_URL}/tipologia?ano=${ano}` : `${API_URL}/tipologia`;
    axios.get(url).then(res => setData(res.data));
  }, [ano]); // Recarrega quando 'ano' muda

  return (
    <div className="chart-container">
      <h3>Tipos de Violência (RF02)</h3>
      <PieChart width={400} height={300}>
        <Pie data={data} cx={200} cy={150} outerRadius={80} fill="#8884d8" dataKey="casos" nameKey="tipo" label>
          {data.map((entry, index) => <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />)}
        </Pie>
        <Tooltip /><Legend />
      </PieChart>
    </div>
  );
}

function GraficoBarrasEstadoComFiltro({ ano }) {
    const [data, setData] = useState([]);
    // Importante: copie o código do seu GraficoBarrasEstado.js aqui ou passe a prop para ele
    // Para facilitar, vou simplificar a lógica de fetch aqui:
    
    useEffect(() => {
        const url = ano ? `${API_URL}/casos_por_estado?ano=${ano}` : `${API_URL}/casos_por_estado`;
        axios.get(url).then(res => {
             const sorted = res.data.sort((a, b) => b.casos - a.casos);
             setData(sorted);
        });
    }, [ano]);

    // ... (Retorne o mesmo JSX do seu gráfico de barras, usando 'data')
    // Se preferir, apenas altere o arquivo GraficoBarrasEstado.js para aceitar a prop {ano}
    // e use axios.get(`${API_URL}/casos_por_estado?ano=${ano}`)
    return (
        <div className="chart-container">
             <h3>Casos por Estado (RF01) - {ano || 'Total'}</h3>
             <p>Dados carregados: {data.length} estados</p>
             {/* Renderize o gráfico aqui igual ao anterior */}
        </div>
    );
}

// --- Componente Principal ---

function App() {
  const [metricas, setMetricas] = useState({});
  const [anoSelecionado, setAnoSelecionado] = useState(""); // Vazio = Todos

  useEffect(() => {
    const url = anoSelecionado ? `${API_URL}/metricas_chave?ano=${anoSelecionado}` : `${API_URL}/metricas_chave`;
    axios.get(url).then(res => setMetricas(res.data));
  }, [anoSelecionado]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Dashboard Violência Contra Mulher (TP5)</h1>
        
        {/* RF04: Filtro de Ano */}
        <div style={{marginTop: '10px'}}>
            <label>Filtrar por Ano: </label>
            <select value={anoSelecionado} onChange={(e) => setAnoSelecionado(e.target.value)} style={{padding: '5px', fontSize: '16px'}}>
                <option value="">Todos os Anos</option>
                <option value="2022">2022</option>
                <option value="2023">2023</option>
            </select>
        </div>
      </header>

      <main>
        <h2>Métricas Chave (RF05)</h2>
        <div className="kpi-grid">
          <KpiCard title="Total de Casos" value={metricas.total_casos_ultimo_ano} />
          <KpiCard title="Média Idade" value={metricas.media_idade_vitimas} />
        </div>

        <div className="charts-grid">
          <GraficoTipologia ano={anoSelecionado} />
          <GraficoTendencia /> {/* Tendencia geralmente mostra todos os anos, não precisa filtrar */}
        </div>

        {/* Importe seu GraficoBarrasEstado e passe a prop ano, ou edite ele para aceitar */}
        <GraficoBarrasEstado ano={anoSelecionado} /> 
      </main>
    </div>
  );
}

export default App;