import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {

  private loginUrl = 'http://localhost:5000/login';

  constructor(private http: HttpClient) { }

  iniciarSesion(usuario: string, contrasena: string): Observable<any> {
    return this.http.post<any>(this.loginUrl, { Usuario: usuario, Contrasena: contrasena });
  }

  private isAuthenticated = false;

  login() {
    this.isAuthenticated = true;
  }

  logout() {
    this.isAuthenticated = false;
  }

  isLoggedIn(): boolean {
    return this.isAuthenticated;
  }

  
}
