import { useState } from 'react'
import './App.css'

function App() {

  const [texto_gemini, set_texto_gemini] = useState('');
  const [consulta, set_consulta] = useState('');
  const [loading, setLoading] = useState(false);

  const enviarNombre = async () => {
    try {
      setLoading(true);
      const res = await fetch('http://localhost:5000/gemini', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ consulta }),
      });

      const data = await res.json();
      set_texto_gemini(data.response);
    } catch (error) {
      console.error('Error al enviar nombre:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div class="input_central">
        <h2>
          ¿Que estas buscando?
        </h2>
        <input type="text" id="input_busqueda" onChange={(e) => set_consulta(e.target.value)}></input>
        <button id='btn_buscar' onClick={enviarNombre} disabled={loading}>
          {loading ? 'Cargando...' : 'Buscar'}
        </button>
      </div>

      <div>
        {loading ? (
          <div className="loading-indicator">
            <div className="spinner"></div>
          </div>
        ) : (
          <h4 style={{ color: 'black' }}>
            {texto_gemini}
          </h4>
        )}
      </div>
    </>
  )
}

export default App
