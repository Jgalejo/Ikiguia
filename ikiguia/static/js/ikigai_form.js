document.addEventListener('DOMContentLoaded', function() {
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.querySelector('button[type="submit"]');
    const progressBar = document.getElementById('progressBar');
    let currentQuestion = 0;
    let questions; // ya no const

    // 1. Envuelve cada <p> como pregunta y marca la primera activa
    document.querySelectorAll('#ikigaiForm p').forEach((p, index) => {
        p.classList.add('question');
        if (index === 0) p.classList.add('active');
    });

    // 2. Ahora sí obtiene el NodeList de preguntas
    questions = Array.from(document.querySelectorAll('.question'));

    function updateProgress() {
        const progress = ((currentQuestion + 1) / questions.length) * 100;
        progressBar.style.width = `${progress}%`;
    }

    function showQuestion() {
        questions.forEach((q, index) => {
            q.classList.toggle('active', index === currentQuestion);
        });
        submitBtn.style.display = currentQuestion === questions.length - 1 ? 'block' : 'none';
        nextBtn.style.display = currentQuestion === questions.length - 1 ? 'none' : 'block';
        updateProgress();
    }

    // Configuración inicial
    showQuestion();

    // Maneja clic en “Siguiente”
    nextBtn.addEventListener('click', function(e) {
        e.preventDefault();
        if (currentQuestion < questions.length - 1) {
            currentQuestion++;
            showQuestion();
        }
    });
});
