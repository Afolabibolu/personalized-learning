import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import { AppLayout } from './components/AppLayout'
import { RequireAuth } from './components/RequireAuth'
import { LoginPage, SignupPage } from './pages/AuthPages'
import { CoursePage } from './pages/CoursePage'
import { HomePage } from './pages/HomePage'
import { LogStudyPage } from './pages/LogStudyPage'
import { OnboardingPage } from './pages/OnboardingPage'
import { QuizPage } from './pages/QuizPage'
import { ResultsPage } from './pages/ResultsPage'
import { TopicPage } from './pages/TopicPage'

const queryClient = new QueryClient({
  defaultOptions: { queries: { staleTime: 30_000, retry: 1, refetchOnWindowFocus: false } },
})

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route
            element={
              <RequireAuth>
                <AppLayout />
              </RequireAuth>
            }
          >
            <Route path="/" element={<HomePage />} />
            <Route path="/onboarding" element={<OnboardingPage />} />
            <Route path="/courses/:courseId" element={<CoursePage />} />
            <Route path="/topics/:topicId" element={<TopicPage />} />
            <Route path="/quiz/:quizId" element={<QuizPage />} />
            <Route path="/attempts/:attemptId" element={<ResultsPage />} />
            <Route path="/log" element={<LogStudyPage />} />
          </Route>
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  )
}
