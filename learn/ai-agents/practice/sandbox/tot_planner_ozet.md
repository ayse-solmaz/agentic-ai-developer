`tot_planner.py`, "Tree of Thoughts" (Düşünce Ağacı) yaklaşımının basitleştirilmiş bir uygulamasını içeren bir planlayıcıdır.

**Temel Özellikleri:**
*   **Çalışma Mantığı:** Verilen bir hedef için LLM kullanarak 3 farklı plan dalı üretir (generator), ardından bu dalları skorlayarak (evaluator) en uygun olanı seçer (search).
*   **Kısıtlar:** Sadece planlama yapar; `tasks.json` dosyasına doğrudan yazma yapmaz, sadece önerilen adımları ekrana basar.
*   **Maliyet:** Her çalışma döngüsünde 2 adet LLM çağrısı (üretim ve değerlendirme) gerçekleştirir.
*   **Güvenlik:** `guardrails.py` modülünü kullanarak girdi ve çıktı denetimi yapar.
*   **Esneklik:** JSON formatındaki çıktıları ayrıştırmak için hata toleranslı bir `parse_json` fonksiyonu içerir.
