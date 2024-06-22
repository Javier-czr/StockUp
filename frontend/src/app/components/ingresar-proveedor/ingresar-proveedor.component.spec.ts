import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IngresarProveedorComponent } from './ingresar-proveedor.component';

describe('IngresarProveedorComponent', () => {
  let component: IngresarProveedorComponent;
  let fixture: ComponentFixture<IngresarProveedorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [IngresarProveedorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(IngresarProveedorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
