import React from 'react';
import { Route, Routes, Navigate, Link, useParams } from 'react-router-dom'
import logo from './logo.svg';
import './App.css';
import { gql, useQuery } from '@apollo/client'

const GET_ALL_CONTENT = gql`
  query GetAllContent {
    allContent {
      title
      slug
    }
  }
`

interface ArticleGQL {
  title: string;
  slug: string;
}

const MainPage = function() {
  const { loading, error, data } = useQuery(GET_ALL_CONTENT);

  if (loading) return <p>Loading ...</p>;
  if (error) return <p>Error :(</p>;
  
  console.log(data)

  const Lists = data.allContent.map((a: ArticleGQL) => (
    <li key={a.slug}><Link to={'article/' + a.slug}>{a.title}</Link></li>
  ));

  return (
    <div className="MainPage">
      <h1>Articles</h1>
      <ul>
        { Lists }
      </ul>
    </div>
  )
}

const GET_ARTICLE = gql`
  query GetArticle($slug: String!) {
    content(slug: $slug) {
      title
      text
      contributors {
        firstName
        lastName
      }
    }
  }
`

const ArticlePage = function() {
  const params = useParams()
  console.log(params);
  const {loading, error, data} = useQuery(GET_ARTICLE, {variables: params})
  
  if (loading) return <p>Loading ...</p>;
  if (error) return <p>Error :(</p>;

  console.log(data)

  return (
    <div className="article">
      <h1> {data.content.title} </h1>
      <div className="body" dangerouslySetInnerHTML={{__html: data.content.text}} />
    </div>
  )
}



function App() {
  return (
    <div className="App">
      <Routes>
        <Route path ='/' element ={<MainPage />} />
        <Route path ='/article/:slug' element={<ArticlePage /> } />
        <Route path='*' element={<Navigate to="/" replace />} />
      </Routes>
    </div>
  );
}

export default App;
