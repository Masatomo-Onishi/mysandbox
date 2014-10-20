/*!
 * \file main.cxx
 * \date Created on: October 9th, 2014
 * \author Masatomo Onishi
 * \brief Hello World program
 */
#include <stdio.h>
#include <stdlib.h>
#include <GL/glut.h>

/**
 * \fn display
 * \brief GL描画関数
 * 窓背景を塗りつぶす。
 */
void display(void)
{
  glClear(GL_COLOR_BUFFER_BIT);
  glBegin(GL_LINE_LOOP);
  glVertex2d(-0.9, -0.9);
  glVertex2d(0.9, -0.9);
  glVertex2d(0.9, 0.9);
  glVertex2d(-0.9, 0.9);
  glEnd(); glFlush();
}

/**
 * \fn init
 * \brief 初期化関数
 */
void init(void)
{
  glClearColor(0.0, 0.0, 1.0, 1.0);
}

/**
 * \fn main
 * \param[in] int 端末からの引数の数
 * \param[in] char** 端末からの引数
 * \brief メイン関数
 */
int main(int argc, char *argv[])
{
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_RGBA);
  glutCreateWindow(argv[0]);
  glutDisplayFunc(display);
  init();
  glutMainLoop();
  return 0R
}
