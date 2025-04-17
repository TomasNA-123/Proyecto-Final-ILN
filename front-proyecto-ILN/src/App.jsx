import { useState } from 'react'
import './App.css'

import Carrusel from './Carrusel'; './Carrusel.jsx'

function App() {

  const [cards, set_cards] = useState([]);
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
      set_cards(
        [...cards, {"datos": data.response}]
        
      );
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

        <div id='contenedor_input'>
          <input type="text" id="input_busqueda" onChange={(e) => set_consulta(e.target.value)} autocomplete="off"></input>
          <button id='btn_buscar' onClick={enviarNombre} disabled={loading}>
            {loading ? 'Cargando...' : 'Buscar'}
          </button>
        </div>
      </div>

      <div>
        {loading ? (
          <div className="loading-indicator">
            <div className="spinner"></div>
          </div>
        ) : (
          <h4 style={{ color: 'black' }}>
            <div id="carrusel_restaurantes">
              <Carrusel cards={cards}></Carrusel>
            </div>
          </h4>
        )}
      </div>
    </>
  )
}

export default App
