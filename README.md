# ⚡ AI Intelligence Multi-Agent System

> Deterministik LangGraph tabanlı, her gün otomatik olarak RSS kaynaklarını ve ArXiv makalelerini toplayan, puanlayan, derinlemesine analiz eden ve GitHub Actions ile arşivleyen otonom yapay zeka istihbarat bülteni.

---

## 🏛️ Mimari ve Akış (System Architecture)

```
   [RSS Feeds / ArXiv API / HF Papers]
                       │
                       ▼
            ┌──────────────────────┐
            │ 1. Ingestion Worker  │ (Async paralel toplama & 24 saatlik tekilleştirme)
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │   2. Curator Agent   │ (Relevance scoring: 1-10 & Pydantic filtreleme)
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │   3. Analyst Agent   │ (Trafilatura ile tam metin kazıma & derin teknik analiz)
            └──────────┬───────────┘
                       ▼
            ┌──────────────────────┐
            │  4. Publisher Agent  │ (Yönetici özeti & Markdown bülten sentezi)
            └──────────┬───────────┘
                       ▼
  [Depolama: reports/YYYY/MM/YYYY-MM-DD-daily-brief.md + README/INDEX.md Güncellemesi]
                       │
                       ▼
         [GitHub Actions Otomatik Git Commit & Push]
```

---

## 🚀 Özellikler

- **Çift LLM Desteği**: Hem Google Gemini hem de OpenAI ile tam uyumlu; `.env` üzerinden tek değişkenle geçiş (`LLM_PROVIDER=gemini` veya `openai`).
- **Kademeli Model Mimarisi**:
  - **Curator Agent**: Hızlı ve düşük maliyetli model (`gemini-2.0-flash` / `gpt-4o-mini`).
  - **Analyst Agent**: Derinlikli mimari, matematik ve benchmark analiz modeli (`gemini-2.0-pro` / `gpt-4o`).
- **Sıfır Halüsinasyon Link Güvencesi**: Raporlardaki bağlantılar asla uydurulmaz; doğrudan Ingestion katmanından gelen gerçek doğrulanmış URL'lerdir.
- **Fail-Safe Veri Toplama**: RSS veya arXiv kaynaklarından biri erişilemez olduğunda pipeline çökmez; hata loglanır ve kalan kaynaklarla devam edilir.
- **Dinamik Web Kazıma (Trafilatura)**: Önemli haberlerin sayfalarına bizzat gidilip tam metin/kod/benchmark bilgisi çekilir.
- **Dil Seçeneği**: Türkçe (`tr`) veya İngilizce (`en`) olarak tek ayarla rapor üretimi.
- **Otonom GitHub Actions**: Her sabah UTC 04:00 (TSİ 07:00) saatinde otomatik çalışır ve repo güncellenir.

---

## 📂 Dizin Yapısı

```
intelligence-agent/
├── .github/
│   └── workflows/
│       └── daily_brief.yml
├── config/
│   ├── sources.yaml
│   └── settings.py
├── src/
│   ├── __init__.py
│   ├── state.py
│   ├── ingest/
│   │   ├── __init__.py
│   │   ├── rss_collector.py
│   │   └── arxiv_collector.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── llm_factory.py
│   │   ├── curator.py
│   │   ├── analyst.py
│   │   └── reporter.py
│   ├── tools/
│   │   ├── __init__.py
│   │   └── web_scraper.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── archive_manager.py
│   └── graph.py
├── reports/
│   └── INDEX.md
├── tests/
├── .env.example
├── Dockerfile
├── requirements.txt
├── README.md
└── main.py
```

---

## ⚙️ Kurulum ve Yerel Çalıştırma

### 1. Depoyu Klonlayın ve Sanal Ortam Oluşturun
```bash
git clone <repo-url>
cd "Haber Takip"

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Çevre Değişkenlerini Ayarlayın
`.env.example` dosyasını `.env` olarak kopyalayın ve API anahtarınızı girin:
```bash
cp .env.example .env
```
Örnek `.env` içeriği:
```ini
LLM_PROVIDER=gemini
GEMINI_API_KEY=AIzaSy...
CURATOR_MODEL=gemini-2.0-flash
ANALYST_MODEL=gemini-2.0-pro
REPORT_LANGUAGE=tr
```

### 3. Pipeline'ı Çalıştırın
```bash
python main.py
```
Özel parametrelerle çalıştırmak için:
```bash
# Belirli bir tarih ve dil ile çalıştırma
python main.py --date 2026-10-19 --lang tr
```

---

## 📰 Son Raporlar Arşivi

<!-- RECENT_REPORTS_START -->
| Tarih | Başlık / Odak Noktası | Rapor Linki |
|:---:|:---|:---:|
| 2026-10-19 | Günlük AI Bülteni | [Raporu Oku](reports/2026/10/2026-10-19-daily-brief.md) |

[Tüm Arşivi Gör (reports/INDEX.md)](reports/INDEX.md)
<!-- RECENT_REPORTS_END -->

---

## 🤖 GitHub Actions ile Otomasyon Kurulumu

1. GitHub deponuzun **Settings > Secrets and variables > Actions** sayfasına gidin.
2. `GEMINI_API_KEY` (veya `OPENAI_API_KEY`) anahtarınızı `Repository secret` olarak ekleyin.
3. **Settings > Actions > General > Workflow permissions** sekmesinden **"Read and write permissions"** seçeneğini etkinleştirin.
4. Sistem her sabah TSİ 07:00'de otomatik olarak raporu derleyip depoya push edecektir!
