import React from 'react';
import './Carrusel.css';

import Card from './Card.jsx';

function Carrusel({ cards }){


    return (
        <>
            <div id='carrusel'>
                {
                    cards.map((card, index) => (
                        <Card key={`card_${index}`} data={card}></Card>
                    ))
                }
            </div>
        </>
    )
}

export default Carrusel