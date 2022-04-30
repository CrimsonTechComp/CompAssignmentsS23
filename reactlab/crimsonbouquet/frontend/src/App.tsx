import React from 'react';
import { Route, Routes, Navigate, Link, useParams } from 'react-router-dom'
import logo from './logo.svg';
import './App.css';
import { gql, useQuery } from '@apollo/client'
import internal from 'stream';


const GET_ALL_CONTENT = gql`
  query GetAllContent {
    allContent {
      title
      slug
    }
  }
`

const GET_ARTICLE = gql`
  query GetArticle($slug: String!) {
    content(slug: $slug) {
      title
      text
      contributors {
        id
        firstName
        lastName      }
    }
  }
`

const GET_CONTRIB = gql`
query GetAllContributors {
  allContributors {
    id
    firstName
    lastName      }
}
`

interface ArticleGQL {
  title: string;
  slug: string;
}

interface ContriGQL {
  id: number;
  firstName: string;
  lastName: string;
}

const MainPage = function() {
  const { loading: contentLoading, error: contentError, data: contentData } = useQuery(GET_ALL_CONTENT);
  const { loading: contribLoading, error: contribError, data: contribData } = useQuery(GET_CONTRIB);

  if (contentLoading || contribLoading) return <p>Loading ...</p>;
  if (contentError || contribError) return <p>Error :(</p>;
  
  console.log(contribData)

  const Lists = contentData.allContent.map((a: ArticleGQL) => (
    <li key={a.slug}><Link to={'article/' + a.slug}>{a.title}</Link></li>
  ));

  const contribLists = contribData.allContributors.map((a: any) => (
    <li key={a.id}>{a.firstName} {a.lastName}</li>
  ));

  return (
    <div className="MainPage">
      <h1>Articles</h1>
      <ul>
        { Lists }
      </ul>
      <h1>Contributors</h1>
      <ul>
        { contribLists }
      </ul>
    </div>
  )
}

const ArticlePage = function() {
  const params = useParams()
  console.log(params);
  const {loading, error, data} = useQuery(GET_ALL_CONTENT, {variables: params})
  
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
