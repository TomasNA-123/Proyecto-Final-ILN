import './Card.css';

function Card({data}){
    return (
        <>
            <div class="card_restaurante">
                {data.datos}
            </div>
        </>
    );
}

export default Card