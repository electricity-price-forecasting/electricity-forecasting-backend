import { Header } from './components/Header/Header'
import { Main } from './components/Main'
import './App.scss';

export const App = () => {
  // return (
  //   <h1>New text</h1>
  // )
  return (
    <div className="App">
      <label htmlFor=""></label>
    <h1>My Page</h1>
    <Header />
    <Main />
  </div>)
}