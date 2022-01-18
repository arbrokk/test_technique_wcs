import logo from './logo.svg';
import './App.css';
import Header from './components/header';
import Footer from "./components/footer";
import Argonautelist from "./components/argonaute_list";


function App() {
  return (
    <div className="App mx-auto h-screen">
        <Header/>
        <main className="mt-6 text-center ">

            <h2 className="text-bold text-2xl ">Ajouter un(e) Argonaute</h2>

            <form className="w-full max-w-sm mx-auto py-4">
                <div className="flex items-center border-b border-red-400 py-2">
                <input id="name"
                className="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
                type="text" placeholder="Nom de l'argonaute" aria-label="nom"/>
                <button
                className="flex-shrink-0 bg-red-400 hover:bg-red-700 border-red-400 hover:border-red-700 text-sm border-4 text-white py-1 px-2 rounded"
                type="Submit">
                Embarquer !
                </button>

                </div>
            </form>

        <Argonautelist/>

        </main>

    <Footer/>
    </div>
  );
}

export default App;
