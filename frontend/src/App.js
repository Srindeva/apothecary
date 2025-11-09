import React, { useEffect, useState } from "react";

function App() {
  const [market, setMarket] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("/market")
      .then(res => {
        if (!res.ok) throw new Error(res.statusText);
        return res.json();
      })
      .then(data => {
        setMarket(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message || "Error fetching market data");
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading market data...</div>;
  if (error) return <div style={{ color: "red" }}>Error: {error}</div>;
  if (!market) return <div>No market data found.</div>;

  // If market is an object, display its properties
  return (
    <div style={{ padding: "2em" }}>
      <h1>Market Information</h1>
      <table style={{ borderCollapse: 'collapse', width: '100%' }}>
        <tbody>
          {Object.entries(market).map(([key, value]) => (
            <tr key={key}>
              <td style={{ fontWeight: "bold", padding: "0.5em", border: "1px solid #ccc" }}>{key}</td>
              <td style={{ padding: "0.5em", border: "1px solid #ccc" }}>{String(value)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;