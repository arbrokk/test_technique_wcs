import logo from './logo.svg';
import './App.css';
import Header from './components/header';

function App() {
  return (
    <div className="App container mx-auto">
        <Header/>
        <main className="mt-6">

            <h2 className="text-bold text-2xl ">Ajouter un(e) Argonaute</h2>

            <form className="w-full max-w-sm mx-auto py-4">
                <div className="flex items-center border-b border-teal-500 py-2">
                <input id="name"
                className="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
                type="text" placeholder="Nom de l'argonaute" aria-label="nom"/>
                <button
                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
                type="Submit">
                Embarquer !
                </button>

                </div>
            </form>


            <h2>Membres de l'équipage</h2>
            <section class="member-list">
            <div class="member-item">Eleftheria</div>
            <div class="member-item">Gennadios</div>
            <div class="member-item">Lysimachos</div>
            </section>
        </main>

      <footer className="">
        <p>Réalisé par Jason en Anthestérion de l'an 515 avant JC</p>
      </footer>
    </div>
  );
}

export default App;
