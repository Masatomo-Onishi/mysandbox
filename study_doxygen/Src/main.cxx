/*!
 * @file main.cxx
 * @date Created on: October 9th, 2014
 * @author Masatomo Onishi
 * @brief Hello World program
 */

#include<iostream>

#include<GL/glut.h>

/*!
 * @fn display
 * @brief GL描画関数
 */
void display(void)
{
}

/*!
 * @fn main
 * @param[in] int
 * @param[in] char**
 * @return 終了状態
 */
int main(int argc, char **argv)
{
  glutInit(&argc, argv);
  glutCreateWindow(argv[0]);
  glutDisplayFunc(display);
  glutMainLoop();
  return 0;
}
