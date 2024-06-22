import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaNotificacionesComponent } from './lista-notificaciones.component';

describe('ListaNotificacionesComponent', () => {
  let component: ListaNotificacionesComponent;
  let fixture: ComponentFixture<ListaNotificacionesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListaNotificacionesComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ListaNotificacionesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
