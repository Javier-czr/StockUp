import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AgregarUbicacionComponent } from './agregar-ubicacion.component';

describe('AgregarUbicacionComponent', () => {
  let component: AgregarUbicacionComponent;
  let fixture: ComponentFixture<AgregarUbicacionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AgregarUbicacionComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AgregarUbicacionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
