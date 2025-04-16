import { useState } from 'react'
import './App.css'

function App() {

  const [texto_gemini, set_texto_gemini] = useState('');
  const [consulta, set_consulta] = useState('');

  const enviarNombre = async () => {
    try {
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
    }
  };

  return (
    <>

    <div class="input_central">
      <h2>
        ¿Que estas buscando?
      </h2>
      <input type="text" id="input_busqueda" onChange={(e) => set_consulta(e.target.value)}></input>
      <button id='btn_buscar' onClick={enviarNombre}>Buscar</button>
    </div>

    <div>
      {texto_gemini}
    </div>
    
    </>
  )
}

export default App
