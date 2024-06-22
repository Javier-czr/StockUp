import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private http: HttpClient, private router: Router, private authService: AuthService) {}

  login() {
    const headers = new HttpHeaders().set('Content-Type', 'application/json');
    const body = { username: this.username, password: this.password };
    this.http.post('http://localhost:5000/login', body, { headers })
      .subscribe(
        (response: any) => {
          console.log('Login exitoso', response);
          this.authService.login();
          this.router.navigate(['/']);  // Redirigir al dashboard u otra página después del login exitoso
        },
        (error) => {
          console.error('Error de login', error);
          if (error.status === 401) {
            alert('Credenciales incorrectas');
          } else {
            alert('Error al intentar iniciar sesión');
          }
        }
      );
  }  

  mostrarRegistro() {
    this.router.navigate(['/registro']);  // Ajusta '/registro' según la ruta de tu componente de registro
  }
}
