<template>
  <div class="home">
    <header>
      <h1>Exam Generator</h1>
    </header>
    <main>
      <section>
        <h2>Upload Document</h2>
        <input type="file" accept=".docx, .pdf" @change="handleFileUpload">
      </section>
      <section v-if="selectedDocument">
        <h2>{{ selectedDocument.name }}</h2>
        <button @click="generateExam">Generate Exam</button>
      </section>
    </main>
    <footer>
      <p>© 2024 Opogen. All rights <a href="https://github.com/Equipo45">reserved</a>.</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedDocument: null,
    };
  },
  methods: {
    handleFileUpload(event) {
      this.selectedDocument = event.target.files[0];
      console.log('MIME type:', this.selectedDocument.type);
    },
    generateExam() {
      if (!this.selectedDocument) {
        // Handle case where no document is selected
        return;
      }

      const formData = new FormData();
      formData.append('file', this.selectedDocument);

      axios.post('http://localhost:5000/generate_exam', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        responseType: 'blob'
      })
        .then(response => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', 'generated_exam.pdf');
          document.body.appendChild(link);
          link.click();
          link.parentNode.removeChild(link); // Clean up
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>
