import { useCallback, useMemo, useState } from 'react'

type Health = 'unknown' | 'ok' | 'fail'

export default function App() {
  const [apiBase, setApiBase] = useState<string>('http://localhost:8000')
  const [health, setHealth] = useState<Health>('unknown')
  const [jsonInput, setJsonInput] = useState<string>(`{
  "feature1": 10,
  "feature2": 0.35,
  "protocol": "TCP"
}`)
  const [result, setResult] = useState<string>('No result yet.')
  const [busy, setBusy] = useState<boolean>(false)

  const healthBadge = useMemo(() => {
    if (health === 'ok') return '<span class="badge ok">ok</span>'
    if (health === 'fail') return '<span class="badge fail">fail</span>'
    return '<span class="badge fail">unknown</span>'
  }, [health])

  const checkHealth = useCallback(async () => {
    try {
      const res = await fetch(`${apiBase}/health`)
      if (!res.ok) throw new Error('Bad status')
      setHealth('ok')
    } catch (e) {
      setHealth('fail')
    }
  }, [apiBase])

  const predict = useCallback(async () => {
    setBusy(true)
    setResult('')
    try {
      const payload = JSON.parse(jsonInput)
      const res = await fetch(`${apiBase}/predict`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data?.detail || 'Prediction failed')
      setResult(JSON.stringify(data, null, 2))
    } catch (e: any) {
      setResult(`Error: ${e?.message || String(e)}`)
    } finally {
      setBusy(false)
    }
  }, [apiBase, jsonInput])

  return (
    <div>
      <div style={{ display: 'none' }} dangerouslySetInnerHTML={{ __html: healthBadge }} id="health-badge" />
      <script dangerouslySetInnerHTML={{ __html: `document.getElementById('health-status').innerHTML = document.getElementById('health-badge').innerHTML;` }} />
      <div style={{ display: 'grid', gap: '1rem', gridTemplateColumns: '1fr 1fr' }}>
        <section>
          <h3>API Health</h3>
          <div id="health-status"><span className="badge fail">unknown</span></div>
          <button onClick={checkHealth}>Check Health</button>
        </section>
        <section>
          <h3>Settings</h3>
          <label>
            API Base URL
            <input value={apiBase} onChange={e => setApiBase(e.target.value)} />
          </label>
        </section>
      </div>

      <section>
        <h3>Predict</h3>
        <p>Paste a single record as JSON. Keys must match your model features.</p>
        <textarea rows={12} value={jsonInput} onChange={e => setJsonInput(e.target.value)} />
        <div style={{ marginTop: '0.5rem' }}>
          <button onClick={predict} aria-busy={busy} disabled={busy}>{busy ? 'Predicting…' : 'Predict'}</button>
        </div>
        <article style={{ marginTop: '1rem' }}>
          <header>Result</header>
          <pre style={{ whiteSpace: 'pre-wrap' }}>{result}</pre>
        </article>
      </section>
    </div>
  )
}


