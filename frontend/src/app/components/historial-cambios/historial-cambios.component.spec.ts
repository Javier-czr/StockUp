import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HistorialCambiosComponent } from './historial-cambios.component';

describe('HistorialCambiosComponent', () => {
  let component: HistorialCambiosComponent;
  let fixture: ComponentFixture<HistorialCambiosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HistorialCambiosComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(HistorialCambiosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
