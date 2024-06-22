import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-registrarse',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './registrarse.component.html',
  styleUrl: './registrarse.component.css'
})
export class RegistrarseComponent {

  usuario: string = '';
  correo: string = '';
  contrasena: string = '';

  constructor(private http: HttpClient) {}

  registrarUsuario() {
    const headers = new HttpHeaders().set('Content-Type', 'application/json');
    const body = {
      Usuario: this.usuario,
      Correo: this.correo,
      Contrasena: this.contrasena
    };

    this.http.post('http://localhost:5000/usuario', body, { headers })
      .subscribe(
        response => {
          console.log('Usuario registrado:', response);
          alert('Usuario registrado exitosamente');
          // Aquí podrías redirigir al usuario a otra página si lo deseas
        },
        error => {
          console.error('Error al registrar usuario:', error);
          alert('Error al registrar usuario');
        }
      );
  }

}
