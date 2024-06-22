import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RealizarPedidosComponent } from './realizar-pedidos.component';

describe('RealizarPedidosComponent', () => {
  let component: RealizarPedidosComponent;
  let fixture: ComponentFixture<RealizarPedidosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RealizarPedidosComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RealizarPedidosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
