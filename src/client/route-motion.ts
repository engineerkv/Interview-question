export function onRouteDidUpdate({
  location,
  previousLocation,
}: {
  location: {pathname: string};
  previousLocation?: {pathname: string} | null;
}): void {
  if (!previousLocation || location.pathname === previousLocation.pathname) {
    return;
  }

  const main = document.querySelector('.main-wrapper');
  if (!(main instanceof HTMLElement)) {
    return;
  }

  main.classList.remove('route-enter');
  void main.offsetWidth;
  main.classList.add('route-enter');
}
