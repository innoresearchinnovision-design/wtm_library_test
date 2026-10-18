document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById('create-modal');
    const modalContainer = document.getElementById('modal-container');
    const openBtn = document.getElementById('open-modal-btn');
    const closeBtns = document.querySelectorAll('.close-modal-btn');

    if (!modal) return; // Exit if modal doesn't exist on this page

    // Open Modal with Smooth Transition
    function openModal() {
        modal.classList.remove('opacity-0', 'pointer-events-none');
        modalContainer.classList.remove('scale-95');
        modalContainer.classList.add('scale-100');
    }

    // Close Modal with Smooth Transition
    function closeModal() {
        modal.classList.add('opacity-0', 'pointer-events-none');
        modalContainer.classList.remove('scale-100');
        modalContainer.classList.add('scale-95');
    }

    // Event Listeners
    if (openBtn) {
        openBtn.addEventListener('click', openModal);
    }

    closeBtns.forEach(btn => {
        btn.addEventListener('click', closeModal);
    });

    // Close when clicking outside the modal box backdrop
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });
});